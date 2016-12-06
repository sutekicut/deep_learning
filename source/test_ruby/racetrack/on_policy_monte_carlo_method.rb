#!/usr/bin/env ruby

#====================
# on_policy_monte_carlo_method.rb
#====================

require './racetrack'
require './course'
require './value'
require './policy'

module Racetrack

  class OnPolicyMonteCarloMethod

    def initialize(course, value, policy, epsilon=0.1)
      @course = course
      @value = value
      @policy = policy
      @epsilon = epsilon
    end

    # エピソードを生成し、方策オン型モンテカルロ法で学習を行う
    # スタートstartが指定されない場合、ランダムに選ぶ
    # learningがfalseの場合、学習を行わない
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
        puts sprintf("position: (%2s, %2s), speed: (%2s, %2s), action: (%2s, %2s), reward: %2d",
                     *(state.split(",")), *(select_action.split(",")), reward) if verbose

        if @course.goal?(next_state)
          puts "total rewards: #{rewards.inject(:+)}" if verbose
          break
        else
          state = next_state
        end
      end

      if learning
        # 価値の更新
        updated = Array.new
        states.pop  # 最後は終端状態なので捨てる
        states.zip(actions).each_with_index do |(state, action), i|
          unless updated.include?([state, action])
            reward_sum = rewards[i, rewards.size - i].inject(:+)
            @value.update(state, action, reward_sum)
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
  opmc_method = Racetrack::OnPolicyMonteCarloMethod.new(course, value, policy, 0.4)
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
  opmc_method = Racetrack::OnPolicyMonteCarloMethod.new(course, value, policy, 0.4)
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