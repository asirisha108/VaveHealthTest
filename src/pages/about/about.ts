import { Component } from '@angular/core';
import { NavController, AlertController } from 'ionic-angular';

@Component({
  selector: 'page-about',
  templateUrl: 'about.html'
})
export class AboutPage {

  constructor(public alertController: AlertController) {

  }

  alertUser() {
  	let alert = this.alertController.create({
		title: 'Custom Alert',
		buttons: ['OK']
	});
	alert.present();
  }
}
