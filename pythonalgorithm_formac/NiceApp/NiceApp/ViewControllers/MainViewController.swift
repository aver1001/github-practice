//
//  ViewController.swift
//  NiceApp
//
//  Created by 박승수 on 2021/07/29.
//

import UIKit
import Lottie

class MainViewController: UIViewController {
    
    let titleLabel: UILabel = {
        let label = UILabel()
        label.textColor = .black
        label.textAlignment = .center
        label.text = "메인화면"
        label.font = UIFont.boldSystemFont(ofSize: 70)
        return label
    }()
    
    let animationView : AnimationView = {
        let animView = AnimationView(name: "70634-concentric-snakes-loader")
        animView.frame = CGRect(x:0,y:0,width: 400,height: 400)
        animView.contentMode = .scaleAspectFit
        return animView
    }()
    //  뷰가 생성되었을떄
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.

        
        view.addSubview(animationView)
        animationView.center = view.center
        // 애니메이션 실행
        animationView.play{(finish) in
            //
            print("애니메이션이 끝났다.")
            self.view.addSubview(self.titleLabel)
            //라벨 위치를 정 가운대로
            self.animationView.removeFromSuperview()
            self.view.addSubview(self.titleLabel)
            
            self.titleLabel.translatesAutoresizingMaskIntoConstraints = false
            self.titleLabel.centerXAnchor.constraint(equalTo: self.view.centerXAnchor).isActive = true
            self.titleLabel.centerYAnchor.constraint(equalTo: self.view.centerYAnchor).isActive = true
        }
    }
}


