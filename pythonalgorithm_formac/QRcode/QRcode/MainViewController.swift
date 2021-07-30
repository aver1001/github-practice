//
//  ViewController.swift
//  QRcode
//
//  Created by 박승수 on 2021/07/29.
//

import UIKit
import WebKit

class MainViewController: UIViewController {

    
    @IBOutlet weak var WebView: WKWebView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        let url = URL (string: "https://www.naver.com")
        let requsetObj = URLRequest(url: url!)
        WebView.load(requsetObj)
    }


}

