#!/usr/bin/env ruby

#====================
# blackjack.rb
#====================

class Blackjack

  # カードとその価値
  # Aceについては、21を越えない限り11として計算する
  CARD = %w(A 2 3 4 5 6 7 8 9 10 J Q K).freeze
  CARD_VALUE = {
    'A'  => 11, '2'  =>  2, '3'  =>  3, '4'  =>  4, '5'  =>  5,
    '6'  =>  6, '7'  =>  7, '8'  =>  8, '9'  =>  9, '10' => 10,
    'J'  => 10, 'Q'  => 10, 'K'  => 10}.freeze

  def initialize
    @player_cards = Array.new
    @player_ace = 0
    @player_total = 0

    @dealer_cards = Array.new
    @dealer_ace = 0
    @dealer_total = 0

    while @player_total < 12
      player_draw
    end

    2.times do
      dealer_draw
    end

    @finish = false
  end

  attr_reader :player_total

  def player_has_ace?
    @player_ace > 0
  end

  def dealer_face_value
    CARD_VALUE[@dealer_cards[0]]
  end

  def player_hit
    raise "Game has finished." if @finish
    player_draw
    @finish = @player_total > 21
  end

  def player_stand
    raise "Game has finished." if @finish
    dealer_draw_all
    @finish = true
  end

  def finish?
    @finish
  end

  # ゲームの結果を返す。
  # +1: プレイヤーの勝ち
  #  0: 引き分け
  # -1: プレイヤーの負け
  def result
    raise "Game hasn't finished." unless @finish
    ret = 0
    if @player_total > 21
      ret = -1
    elsif @dealer_total > 21
      ret = 1
    elsif @player_total > @dealer_total
      ret = 1
    elsif @player_total < @dealer_total
      ret = -1
    else
      ret = 0
    end
    return ret
  end

  def print
    puts "-" * 20
    puts "Player (total: #{@player_total}) [#{@player_cards.map{|c| sprintf("%2s", c)}.join(', ')}]"
    if @finish
      puts "Dealer (total: #{@dealer_total}) [#{@dealer_cards.map{|c| sprintf("%2s", c)}.join(', ')}]"
    else
      puts "Dealer (total: ??) [#{sprintf "%2s", @dealer_cards[0]}, ??]"
    end
    puts "-" * 20
  end

  private

  def draw_card
    return CARD.sample
  end

  def player_draw
    card = draw_card
    @player_cards.push(card)
    @player_ace += 1 if card == 'A'
    @player_total += CARD_VALUE[card]
    if (@player_total > 21) && (@player_ace > 0)
      @player_total -= 10
      @player_ace -=1
    end
  end

  def dealer_draw
    card = draw_card
    @dealer_cards.push(card)
    @dealer_ace += 1 if card == 'A'
    @dealer_total += CARD_VALUE[card]
    if (@dealer_total > 21) && (@dealer_ace > 0)
      @dealer_total -= 10
      @dealer_ace -=1
    end
  end

  def dealer_draw_all
    while @dealer_total < 17
      dealer_draw
    end
  end
end

if __FILE__ == $PROGRAM_NAME
  game = Blackjack.new
  loop do
    game.print
    puts "select..."
    puts "[h] hit"
    puts "[s] stand"
    puts "[q] quit"

    input = STDIN.gets[0]
    case input
    when 'h'
      game.player_hit
    when 's'
      game.player_stand
    when 'q'
      exit
    else
      puts "wrong input!"
    end

    if game.finish?
      break
    end
  end

  game.print
  result = game.result
  if result > 0
    puts "Player win!"
  elsif result < 0
    puts "Player lose!"
  else
    puts "Draw."
  end
end