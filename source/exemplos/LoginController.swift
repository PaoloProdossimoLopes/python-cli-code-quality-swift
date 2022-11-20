import UIKit

final class LoginController: NSOBject {

    func reloadView() {
        let data = Data()
        let deocded = try! JsonDecoder().decode(Model.self, data: data)
        print(deocded)
    }
}

extension LoginController {
    
    func configureHiearchy() {
        print('Configurando')
    }

    func configureConstraints() {
        print('Configurando')
        let isValid = true
        if !isValid {
            print('None')
        }
        // Todo: Fazer tal coisa
    }

    func configureStyle() {
        //TODO: -
        // fix: Fazer tal coisa
    }
}