#!/usr/bin/env ruby

#====================
# mces_method.rb
#====================

require './blackjack'
require './action_value'
require './policy'

# モンテカルロ-ES法
class MCESMethod

  def initialize(action_value, policy)
    @action_value = action_value
    @policy = policy
  end

  attr_reader :action_value, :policy

  # 1ゲーム行い、価値関数と方策を更新する
  def simulate(verbose=false)
    game = Blackjack.new
    game.print if verbose

    player_total_queue = Array.new
    player_has_ace_queue = Array.new
    player_hit_queue = Array.new
    dealer_face_value = game.dealer_face_value

    # エピソード生成
    loop do
      player_total = game.player_total
      player_has_ace = game.player_has_ace?

      # 一番最初の行動は、開始点探査の仮定を満たすために、
      # ランダムに選択する
      if player_hit_queue.empty?
        player_hit = [true, false].sample
      else
        player_hit = @policy.hit?(player_total, player_has_ace, dealer_face_value)
      end

      player_total_queue.push(player_total)
      player_has_ace_queue.push(player_has_ace)
      player_hit_queue.push(player_hit)

      if player_hit
        game.player_hit
        game.print if verbose
        break if game.finish?
      else
        game.player_stand
        game.print if verbose
        break
      end
    end

    # 価値関数の更新
    result = game.result
    player_total_queue.zip(player_has_ace_queue, player_hit_queue) do |player_total, player_has_ace, player_hit|
      @action_value.update(player_total, player_has_ace, dealer_face_value, player_hit, result)
    end

    # 方策の更新
    player_total_queue.zip(player_has_ace_queue) do |player_total, player_has_ace|
      hit_value = @action_value.get(player_total, player_has_ace, dealer_face_value, true)
      stand_value = @action_value.get(player_total, player_has_ace, dealer_face_value, false)
      if hit_value > stand_value
        @policy.set(player_total, player_has_ace, dealer_face_value, true)
      elsif hit_value < stand_value
        @policy.set(player_total, player_has_ace, dealer_face_value, false)
      end
    end
  end

end

if __FILE__ == $PROGRAM_NAME
  value = ActionValue.new
  policy = Policy.new
  mces = MCESMethod.new(value, policy)
  (1..10).each do |i|
    100000.times do
      mces.simulate
    end
    puts "[#{i * 100000}]"
    mces.action_value.print
    mces.policy.print
  end
end