import { Component, OnInit } from '@angular/core';
import { CadastroService, IAllUsers, INewUser, INewImages, IImageAux } from './cadastro.service';
import { FormGroup, Validators } from '@angular/forms';
import { FormBuilder } from '@angular/forms';
import { Observable, Subscriber } from 'rxjs';

import { DomSanitizer, SafeUrl } from '@angular/platform-browser';
@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro.component.html',
  styleUrls: ['./cadastro.component.css']
})
export class CadastroComponent implements OnInit {
  form!: FormGroup;
  myImage!:Observable<any>;
  myImageAux!:string
  MyImageSafe!: SafeUrl[];
  base64code!:any

  onChange = ($event: Event) => {
    const target = $event.target as HTMLInputElement;

    const file: File = (target.files as FileList)[0];


    this.convertToBase64(file)
  }

  convertToBase64(file: File) {

    const observable = new Observable((subscriber: Subscriber<any>)=> {
       this.readFile(file,subscriber)
    })

    observable.subscribe((d)=> {
      console.log(d)
      this.myImage = d 
      this.base64code = d
    })

  }

  convertToImage(observable:Observable<any>) {



  }

  readFile(file: File, subscriber: Subscriber<any>) {

    const filerreader = new FileReader();

    filerreader.readAsDataURL(file)

    filerreader.onload = () => {
      subscriber.next(filerreader.result);

      subscriber.complete()
    }

    filerreader.onerror = () => {
      subscriber.error()
      subscriber.complete()

    }
  }

  userSourcer: IAllUsers[] = [];
  newUser: INewUser = {} as INewUser
  uploadedFiles: any[] = [];

  constructor(
    private cadastroService : CadastroService,
    private formBuilder: FormBuilder,
    private sanatizer: DomSanitizer
  ) { }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      name: [null, Validators.required],
      image: [null, Validators.required],
    });
    this.listAllUsers();
  }


  listAllUsers(){
    this.cadastroService
    .listarTodosUsuarios()
    .subscribe((resp) => {
      this.userSourcer = resp;
      if (this.userSourcer.length > 0) {
        this.userSourcer.forEach((user) => {
          if (user.images != undefined) {
            if (user.images.length > 0){
              user.images.forEach((userImage) => {
                this.myImageAux = userImage.base64.replace(/data/g,"data:")
                this.myImageAux = this.myImageAux
                this.myImageAux = this.myImageAux.replace(/jpegbase64/g,"jpeg;base64,")
                this.sanatizer.bypassSecurityTrustUrl(userImage.base64)
                userImage.base64Safe = this.sanatizer.bypassSecurityTrustUrl(this.myImageAux)
              })
              
              // this.myImageAux = user.images.map(
              //   ({ base64 }) => ({ base64 })
              // )

            }
          }
        }

        )
      }

    });
    
    // => {
    //   (this.userSourcer = resp),
    //   if (this.userSourcer.length > 0) {

    //   }

    //   // this.myImageAux = this.userSourcer[0].images[0].base64.replace(/data/g,"data:")
    //   // this.myImageAux = this.myImageAux.replace(/jpegbase64/g,"jpeg;base64,")
     
    //   // this.MyImageSafe = this.sanatizer.bypassSecurityTrustUrl(this.myImageAux)
    // });
  }

  InputUsuario(){
    this.newUser.name = this.form.value.name
    this.newUser.images = [{
      base64: this.base64code
    }]
      this.cadastroService
    .cadastrarUsuario(this.newUser)
    .subscribe(() => {
      this.listAllUsers();
    }
    );
    
  }


}
