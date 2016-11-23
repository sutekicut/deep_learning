#====================
# policy.rb
#====================

require './blackjack'

class Policy
  def initialize
    @policy = Array.new(2) do
      Hash.new do |player, total|
        player[total] = Hash.new do |dealer, face|
          dealer[face] = true
        end
      end
    end
  end

  def hit?(player_total, player_has_ace, dealer_face_value)
    ace_index = player_has_ace ? 0 : 1
    @policy[ace_index][player_total][dealer_face_value]
  end

  def set(player_total, player_has_ace, dealer_face_value, hit)
    ace_index = player_has_ace ? 0 : 1
    @policy[ace_index][player_total][dealer_face_value] = hit
  end

  @@print_bar    = "---"  + "------" * (12..21).size
  @@print_header = "  |"  + sprintf("    %2d" * (12..21).size, *((12..21).to_a))
  @@print_format = "%2d|" + " %5s" * (12..21).size + "\n"

  def print
    puts @@print_bar.sub("-" * "[ace]".size, "[ace]")
    puts @@print_header
    puts @@print_bar
    (2..11).each do |dealer_face_value|
      printf @@print_format,
        dealer_face_value,
        *((12..21).map{|player_total| hit?(player_total, true, dealer_face_value) ? 'hit' : 'stand'})
    end
    puts @@print_bar

    puts @@print_bar.sub("-" * "[no ace]".size, "[no ace]")
    puts @@print_header
    puts @@print_bar
    (2..11).each do |dealer_face_value|
      printf @@print_format,
        dealer_face_value,
        *((12..21).map{|player_total| hit?(player_total, false, dealer_face_value) ? 'hit' : 'stand'})
    end
    puts @@print_bar
  end
end