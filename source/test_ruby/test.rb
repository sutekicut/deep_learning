class StatusValue
    # 状態価値の初期値は0
    def initialize
      @count = 0
      @value = Array.new((0..20).size) do
        Array.new((0..20).size, 0.0)
        @count = @count + 1
      end
    end

    def get_most_valuable_move(x, y, *move_list)
      move_value_hash = move_list.each_with_object(Hash.new) do |move, hash|
        begin

          hash[move] = move
        rescue
          #不正な移動の場合、処理をスキップ
        end
      end

      return move_value_hash
    end

    def print
      puts @value
    end
end

if __FILE__ == $PROGRAM_NAME
  status_value = StatusValue.new
  # status_value.print
  hash = status_value.get_most_valuable_move(5, 4, 1)
  puts hash

end
