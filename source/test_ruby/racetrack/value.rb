#====================
# value.rb
#====================

require './racetrack'
require './course'

module Racetrack

  class Value

    # 方策オフ型モンテカルロ法でも使えるように、
    # 行動価値を出すための分子(points: 収益に重み付けしたものの合計)と
    # 分母(weights: 重みの合計)を保持する。
    def initialize
      @value = Hash.new do |hash, state|
        hash[state] = Hash.new do |hash, action|
          hash[action] = 0.0
        end
      end
      @points = Hash.new do |hash, state|
        hash[state] = Hash.new do |hash, action|
          hash[action] = 0.0
        end
      end
      @weights = Hash.new do |hash, state|
        hash[state] = Hash.new do |hash, action|
          hash[action] = 0.0
        end
      end
    end

    def get(state, action)
      @value[state][action]
    end

    def get_max_action(state)
      hash = @value[state]
      max_value = hash.values.max
      max_action = hash.key(max_value)
      return max_action
    end

    def update(state, action, reward, weight=1.0)
      @points[state][action] += reward * weight
      @weights[state][action] += weight
      @value[state][action] = @points[state][action] / @weights[state][action]
    end

  end

end