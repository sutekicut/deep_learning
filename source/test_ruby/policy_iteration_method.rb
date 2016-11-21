#!/usr/bin/env ruby

#====================
# policy_iteration_method.rb
#====================

require './rental_car_problem'
require './status_value'
require './policy'

module RentalCarProblem
  # 方策反復法
  class PolicyIterationMethod
    def initialize(value, policy, verbose=false)
      @value = value
      @policy = policy
      @verbose = verbose
    end

    attr_reader :value, :policy

    def execute
      i = 0
      loop do
        evaluate_policy
        if @verbose
          puts "Value_#{i}"
          @value.print
        end

        improved = improve_policy
        if @verbose
          puts "Policy_#{i}"
          @policy.print
        end

        if improved
          i += 1
        else
          break
        end
      end
    end

    private

    @@delta_max = 0.1

    # 方策policyで方策評価を行う
    def evaluate_policy
      loop do
        delta = 0.0

        (0..RENTAL_CAR_MAX).each do |x|
          (0..RENTAL_CAR_MAX).each do |y|
            old_value = @value.get(x, y)
            new_value = @value.value_of_move(x, y, policy.get(x, y))

            delta = [delta, (new_value - old_value).abs].max
            @value.set(x, y, new_value)
          end
        end

        if delta < @@delta_max
          break
        end

        @value.print if @verbose
      end
    end

    # 状態価値valueを使って方策改善を行う
    # 改善された場合trueを返す
    def improve_policy
      policy_improved = false

      (0..RENTAL_CAR_MAX).each do |x|
        (0..RENTAL_CAR_MAX).each do |y|
          old_policy = @policy.get(x, y)

          new_policy, max_value = @value.get_most_valuable_move(x, y, *((-MOVE_MAX..MOVE_MAX).to_a))

          if old_policy != new_policy
            policy_improved = true
            @policy.set(x, y, new_policy)
          end
        end
      end

      return policy_improved
    end
  end
end

if __FILE__ == $PROGRAM_NAME
  include RentalCarProblem

  value = StatusValue.new
  policy = Policy.new
  policy_iteration = PolicyIterationMethod.new(value, policy, true)

  policy_iteration.execute

  puts "最適状態価値関数"
  policy_iteration.value.print

  puts "最適方策"
  policy_iteration.policy.print
end