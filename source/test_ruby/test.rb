require 'awesome_print'

if __FILE__ == $PROGRAM_NAME
  (2..11).each do |dealer_face_value|
    puts dealer_face_value



  end



#  value = Array.new(2) do
#    Hash.new do |player, total|
#      player[total] = Hash.new do |dealer, face|
#        dealer[face] = Array.new(2, 0.0)
#      end
#    end
#  end
#
#  test = Array.new(2) do
#    Hash.new do |hash, key|
#      hash["test"] = "test"
#    end
#  end
#
#  value.each do |hash, idx|
#    puts "#{idx}: #{hash}"
#    hash.each do |value, key|
#      puts "#{key}: #{value}"
#    end
#  end
#
#  test.each do |hash, idx|
#    puts "#{idx}: #{hash}"
#    hash.each do |value, key|
#      puts "#{key}: #{value}"
#    end
#  end
#
#  ap value
#  ap test

end
