import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { SafeUrl } from '@angular/platform-browser';

export interface IAllUsers {
  name: string;
  id: number;
  images: IImages[];
}
export interface IImages {
  base64: string;
  id: number;
  user_id: number;
  base64Safe: SafeUrl
}

export interface INewUser {
  name: string
  images: INewImages[];
}

export interface INewImages {
  base64: Observable<any>;
}

export interface IImageAux {
  base64: string;
}




@Injectable({
  providedIn: 'root',
})

export class CadastroService {
  pathUrlBase = 'http://localhost:8000'
  constructor(private http: HttpClient) { }



  listarTodosUsuarios(): Observable<IAllUsers[]> {
    return this.http.get<IAllUsers[]>(
      `${this.pathUrlBase}/users`
    );
  }

  listaUsuarioPorId(
    id: number
  ): Observable<IAllUsers> {
    return this.http.post<IAllUsers>(
      `${this.pathUrlBase}/users`,
      { id }
    );
  }



  cadastrarUsuario(
    newUser: INewUser
  ): Observable<IAllUsers> {
    console.log(newUser)
    return this.http.post<IAllUsers>(
      `${this.pathUrlBase}/users`,
      { ...newUser }
    );
  }

}



