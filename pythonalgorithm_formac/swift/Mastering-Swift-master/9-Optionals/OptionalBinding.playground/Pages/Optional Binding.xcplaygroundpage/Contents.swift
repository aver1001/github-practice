//
//  Copyright (c) 2018 KxCoding <kky0317@gmail.com>
//
//  Permission is hereby granted, free of charge, to any person obtaining a copy
//  of this software and associated documentation files (the "Software"), to deal
//  in the Software without restriction, including without limitation the rights
//  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
//  copies of the Software, and to permit persons to whom the Software is
//  furnished to do so, subject to the following conditions:
//
//  The above copyright notice and this permission notice shall be included in
//  all copies or substantial portions of the Software.
//
//  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
//  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
//  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
//  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
//  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
//  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
//  THE SOFTWARE.
//
import Foundation

/*:
 # Optional Binding
 */



var num: Int? = nil
print(num!)











/*:
 ## Syntax
 ![optional-binding-syntax](optional-binding-syntax.png)
 */


if num != nil{
    print(num!)
}else{
    print("empty")
}

//값이 리턴이 되면 unrapping 후 값 저장.
//강제추출대신 Optional Binding 사용해야함.

if let n = num {
    print(n)
}else{
    print("empty")
}


var str: String? = "str"
guard let str = str else {
    fatalError()
}

//guard 문은 else block 다음부터 상수 사용 가능

// let 상수 var 변수

num = 123
if var num = num {
    num = 456
    print(num)
}

let a: Int? = 12
let b: String? = "str"

// 모두 binding 되었을시 실행
if let num = 1, let str = b ,str.count > 5{
    
}








































