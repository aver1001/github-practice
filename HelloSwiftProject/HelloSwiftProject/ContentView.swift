//
//  ContentView.swift
//  HelloSwiftProject
//
//  Created by 박승수 on 2021/06/30.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        Text("Hello, world!")
        Button(action: /*@START_MENU_TOKEN@*//*@PLACEHOLDER=Action@*/{}/*@END_MENU_TOKEN@*/) {
            /*@START_MENU_TOKEN@*//*@PLACEHOLDER=Content@*/Text("Button")/*@END_MENU_TOKEN@*/
        }
            .padding()
    }
}
struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        Group {
            ContentView()
            
        }
    }
}
