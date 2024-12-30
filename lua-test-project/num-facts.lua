-- THIS PROGRAM GIVES THE USER SIMPLE FACTS ABOUT A NUMBER THEY ENTER

-- is_prime(num)
-- num : input of type number
-- output : true if num is prime, false if not
function Is_prime(num)
    for i = 2, math.sqrt(num), 1 do
        if num % i == 0 then
            return false
        end
    end

    return true
end

-- factorial(num)
-- num : input of type number
-- output : factorial of num
function Factorial(num)
    if num == 0 then
        return 1
    else
        return num * Factorial(num - 1)
    end
end

-- perfect_cube(num)
-- num : input of type number
-- output : the third root of num if num is a perfect cube, false if not
function Perfect_cube(num)
    local i = 1
    while i^3 <= num do
        if i^3 == num then
            return i
        end

        i = i + 1
    end
    return false
end

print('Welcome! Please enter your number below:')
local userNumber = tonumber(io.read())

if userNumber % 2 == 0 then
    print('This is an even number')
    
    if userNumber ~= 2 then
        print('This number is not a prime')
    else
        print('This number is a prime')
    end

else
    print('This is an odd number')

    if Is_prime(userNumber) then
        print('This number is a prime')
    else
        print('This number is not a prime')
    end
end 

if (math.floor(math.sqrt(userNumber))) == math.sqrt(userNumber) then
    print('This number is a perfect square. Its square root is', tonumber(math.sqrt(userNumber)))
else
    print('This number is not a perfect square')
end

if Perfect_cube(userNumber) ~= false then
    print('This number is a perfect cube. Its third root is', Perfect_cube(userNumber))
else
    print('This number is not a perfect cube')
end

print('The factorial of this number is:', Factorial(userNumber))