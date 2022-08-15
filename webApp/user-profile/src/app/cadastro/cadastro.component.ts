import { Component, OnInit } from '@angular/core';
import { CadastroService, IAllUsers } from './cadastro.service';
import { FormGroup, Validators } from '@angular/forms';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro.component.html',
  styleUrls: ['./cadastro.component.css']
})
export class CadastroComponent implements OnInit {
  form!: FormGroup;

  userSourcer: IAllUsers[] = [];

  constructor(
    private cadastroService : CadastroService,
    private formBuilder: FormBuilder
  ) { }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      name: [null, Validators.required],
    });
    this.listAllUsers();
    console.log(this.userSourcer)
  }


  listAllUsers(){
    this.cadastroService
    .listarTodosUsuarios()
    .subscribe((resp) => {
      console.log(resp);
      (this.userSourcer = resp)});
  }

  cadastrarUsuario(){
    this.cadastroService
    .cadastrarUsuario(this.form.value)
    .subscribe(() => {});
    this.listAllUsers();
  }

}
