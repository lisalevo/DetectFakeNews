import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { RoutingModule } from './/routing.module';
import { TimestampComponent } from './timestamp/timestamp.component';
import { VideoViewerComponent } from './video-viewer/video-viewer.component';
import { SpeechViewerComponent } from './speech-viewer/speech-viewer.component';
import { FactSummaryComponent } from './fact-summary/fact-summary.component';
import { PowerbiComponent } from './powerbi/powerbi.component';

@NgModule({
  declarations: [AppComponent, TimestampComponent, VideoViewerComponent, SpeechViewerComponent, FactSummaryComponent, PowerbiComponent],
  imports: [BrowserModule, RoutingModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
