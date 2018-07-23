import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { RoutingModule } from './/routing.module';

@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule, RoutingModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
