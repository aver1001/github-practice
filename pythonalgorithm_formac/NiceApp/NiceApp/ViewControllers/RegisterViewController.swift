//
//  RegisterViewController.swift
//  NiceApp
//
//  Created by 박승수 on 2021/07/29.
//

import UIKit

class RegisterViewController: UIViewController {
    @IBOutlet weak var btnForLogingViewController: UIButton!
    
    //  뷰가 생성되었을떄
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        //네비게이션 바를 숨길것인가?
        self.navigationController?.isNavigationBarHidden = true
    }
    @IBAction func onLoginViewControllerbtnClick(_ sender: UIButton) {
        print("RegisterViewController - onLogingViewContorllerBtnClicked() called / 로그인 버튼 클릭 !!")
        //네비게이션 뷰 컨트롤러를 팝 한다.
        self.navigationController?.popViewController(animated: true)
    }
    
}
