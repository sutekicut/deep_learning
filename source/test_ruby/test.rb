class StatusValue
    # 状態価値の初期値は0
    def initialize
      @count = 0
      @value = Array.new((0..20).size) do
        Array.new((0..20).size, 0.0)
        @count = @count + 1
        # puts @count
      end

      puts @value
    end

    def print
      puts @value
    end
end

if __FILE__ == $PROGRAM_NAME
  # status_value = StatusValue.new
  # status_value.print
  puts (0..10).size
end
