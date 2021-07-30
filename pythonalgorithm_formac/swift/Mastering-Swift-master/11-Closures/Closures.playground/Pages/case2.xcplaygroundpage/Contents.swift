//: [Previous](@previous)

import Foundation

print("Start")
print("End")

DispatchQueue.main.asyncAfter(deadline: .now()+5, execute: {
    print("End")
})


