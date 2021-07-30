//
//  ViewController.swift
//  Practice
//
//  Created by 박승수 on 2021/06/30.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var lbl: UILabel!
    @IBAction func changeLabel(_ sender: Any) {
        lbl.text = "안녕하세요"
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }


}

