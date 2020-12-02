file = File.open('input.txt')
file_data = file.readlines.map(&:chomp)

counter = 0

for item in file_data
  seperated = item.split
  
  numbersPart = seperated[0].split('-')
  startNum = numbersPart[0].to_i
  endNum = numbersPart[1].to_i
  
  charToCheck = seperated[1].split(':')[0]

  passwordToCheck = seperated[2].split('')

  charCounter = 0

  for c in passwordToCheck
    if c == charToCheck
      charCounter += 1
    end
  end
  
  if charCounter >= startNum && charCounter <= endNum
    counter += 1
  end
end

print "Result part 1: " + counter.to_s  + "\n\n\n"


counter = 0

for item in file_data
  seperated = item.split
  
  numbersPart = seperated[0].split('-')
  startNum = numbersPart[0].to_i - 1
  endNum = numbersPart[1].to_i - 1
  
  charToCheck = seperated[1].split(':')[0]

  passwordToCheck = seperated[2].split('')

  charCorrect = false
  
  if (passwordToCheck[startNum] == charToCheck) ^ (passwordToCheck[endNum] == charToCheck)
    charCorrect = true
  end

  if charCorrect
    counter += 1
  end
end

print "Result part 2: " + counter.to_s  + "\n\n\n"