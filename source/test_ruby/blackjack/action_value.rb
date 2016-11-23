#====================
# action_value.rb
#====================

require './blackjack'

class ActionValue
  def initialize
    @value = Array.new(2) do
      Hash.new do |player, total|
        player[total] = Hash.new do |dealer, face|
          dealer[face] = Array.new(2, 0.0)
        end
      end
    end

    @count = Array.new(2) do
      Hash.new do |player, total|
        player[total] = Hash.new do |dealer, face|
          dealer[face] = Array.new(2, 0)
        end
      end
    end


  end

  def get(player_total, player_has_ace, dealer_face_value, player_hit)
    ace_index = player_has_ace ? 0 : 1
    action_index = player_hit ? 0 : 1
    @value[ace_index][player_total][dealer_face_value][action_index]
  end

  def update(player_total, player_has_ace, dealer_face_value, player_hit, reward)
    ace_index = player_has_ace ? 0 : 1
    action_index = player_hit ? 0 : 1

    count = @count[ace_index][player_total][dealer_face_value][action_index]
    count += 1
    @count[ace_index][player_total][dealer_face_value][action_index] = count

    value = @value[ace_index][player_total][dealer_face_value][action_index]
    value += (1.0 / count) * (reward - value)
    @value[ace_index][player_total][dealer_face_value][action_index] = value
  end

  @@print_bar    = "---"  + "------------" * (12..21).size
  @@print_header = "  |"  + sprintf("   %2d(h/s)  " * (12..21).size, *((12..21).to_a))
  @@print_format = "%2d|" + " % 4.2f/% 4.2f" * (12..21).size + "\n"

  def print
    puts @@print_bar.sub("-" * "[ace]".size, "[ace]")
    puts @@print_header
    puts @@print_bar
    (2..11).each do |dealer_face_value|
      printf @@print_format,
        dealer_face_value,
        *(
          (12..21).map do |player_total|
            [
              get(player_total, true, dealer_face_value, true),
              get(player_total, true, dealer_face_value, false)
            ]
          end.flatten
        )
    end
    puts @@print_bar

    puts @@print_bar.sub("-" * "[no ace]".size, "[no ace]")
    puts @@print_header
    puts @@print_bar
    (2..11).each do |dealer_face_value|
      printf @@print_format,
        dealer_face_value,
        *(
          (12..21).map do |player_total|
            [
              get(player_total, false, dealer_face_value, true),
              get(player_total, false, dealer_face_value, false)
            ]
          end.flatten
        )
    end
    puts @@print_bar
  end
end