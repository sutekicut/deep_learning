#====================
# policy.rb
#====================

require './racetrack'
require './course'

module Racetrack

  class Policy

    # 初期の方策は可能な行動からランダムに選択する
    def initialize(course)
      @course = course
      @policy = Hash.new do |hash, state|
        valid_actions = @course.get_valid_actions(state)
        hash[state] = valid_actions.sample
      end
    end

    def get(state)
      @policy[state]
    end

    def set(state, action)
      @policy[state] = action
    end

  end

end