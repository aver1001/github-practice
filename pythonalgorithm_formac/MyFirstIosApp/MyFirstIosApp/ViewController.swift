//
//  ViewController.swift
//  MyFirstIosApp
//
//  Created by 박승수 on 2021/07/29.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet var tableView :UITableView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.tableView.backgroundColor = UIColor.red
    }

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) {
      return 100
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) {
      let cell = UITableViewCell()
      cell.textField?.text = "\(indexPath.row)"
      return cell
    }
}

