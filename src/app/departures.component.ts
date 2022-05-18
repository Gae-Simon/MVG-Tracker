import {Component} from "@angular/core";

@Component({
  selector: 'app-departure',
  template: '<h4 style="text-align: center">{{ getTitle() }}</h4>'
})
export class DeparturesComponent{
  title = "Departure1";

  getTitle(){
    return this.title;
  }
}
