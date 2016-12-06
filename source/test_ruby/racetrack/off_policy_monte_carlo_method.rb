#!/usr/bin/env ruby

#====================
# off_policy_monte_carlo_method.rb
#====================

require './racetrack'
require './course'
require './value'
require './policy'

module Racetrack

  class OffPolicyMonteCarloMethod

    def initialize(course, value, policy, epsilon=0.1)
      @course = course
      @value = value
      @policy = policy
      @epsilon = 0.1
    end

    # エピソードを生成し、方策オフ型モンテカルロ法で学習を行う
    # スタートstartが指定されない場合、ランダムに選ぶ
    # learningがfalseの場合、ソフト方策を使わず、学習を行わない
    def simulate(start=nil, learning=true, verbose=false)
      if start == nil
        starts = @course.starts
        start = starts.sample
      end

      states = Array.new
      actions = Array.new
      rewards = Array.new

      # エピソードを生成
      state = start
      states.push state
      loop do
        valid_actions = @course.get_valid_actions(state)

        select_action = @policy.get(state)
        if learning
          select = Random.rand
          valid_actions.each_with_index do |action, i|
            if select < ((@epsilon / valid_actions.size) * (i + 1))
              select_action = action
              break
            end
          end
        end
        actions.push select_action

        next_state, reward = @course.step(state, select_action)
        states.push next_state
        rewards.push reward

        if @course.goal?(next_state)
          puts "total rewards: #{rewards.inject(:+)}" if verbose
          break
        else
          state = next_state
        end
      end

      # 価値と方策の更新
      if learning
        # 後ろから更新に必要な情報を作っていく
        update_info = Array.new
        states.pop # 最後は終端状態なので捨てる
        state = states.pop
        action = actions.pop
        reward_sum = rewards.pop
        weight = 1.0
        loop do
          actions_size = @course.get_valid_actions(state).size
          if action == @policy.get(state)
            update_info.unshift([state, action, reward_sum, weight])
            if states.empty?
              break
            else
              state = states.pop
              action = actions.pop
              reward_sum += rewards.pop
              weight *= 1.0 / ((1 - @epsilon) + (@epsilon / actions_size))
            end
          else
            update_info.unshift([state, action, reward_sum, weight])
            break
          end
        end

        # 価値を更新
        updated = Array.new
        update_info.each do |state, action, reward_sum, weight|
          unless updated.include?([state, action])
            @value.update(state, action, reward_sum, weight)
            updated.push([state, action])
          end
        end

        # 方策の更新
        updated.each do |state, action|
          max_action = @value.get_max_action(state)
          @policy.set(state, max_action)
        end
      end
    end

  end

end

if __FILE__ == $PROGRAM_NAME
  # コース1
  puts "------------------------------"
  puts "コース1"
  puts "------------------------------"
  course = Racetrack::Course.new(COURSE1)
  value = Racetrack::Value.new
  policy = Racetrack::Policy.new(course)
  opmc_method = Racetrack::OffPolicyMonteCarloMethod.new(course, value, policy, 0.4)
  (1..10).each do |i|
    10000.times do
      opmc_method.simulate
    end
    puts "--------------------"
    puts "[#{i * 10000}]"
    puts "--------------------"
    course.starts.each do |start|
      puts "----------"
      puts "<start: #{start}>"
      opmc_method.simulate(start, false, true)
      puts "----------"
    end
  end

  # コース2
  puts "------------------------------"
  puts "コース2"
  puts "------------------------------"
  course = Racetrack::Course.new(COURSE2)
  value = Racetrack::Value.new
  policy = Racetrack::Policy.new(course)
  opmc_method = Racetrack::OffPolicyMonteCarloMethod.new(course, value, policy, 0.4)
  (1..10).each do |i|
    10000.times do
      opmc_method.simulate
    end
    puts "--------------------"
    puts "[#{i * 10000}]"
    puts "--------------------"
    course.starts.each do |start|
      puts "----------"
      puts "<start: #{start}>"
      opmc_method.simulate(start, false, true)
      puts "----------"
    end
  end

end