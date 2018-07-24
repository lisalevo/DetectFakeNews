import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { RoutingModule } from './/routing.module';
import { TimestampComponent } from './timestamp/timestamp.component';
import { VideoViewerComponent } from './video-viewer/video-viewer.component';
import { SpeechViewerComponent } from './speech-viewer/speech-viewer.component';
import { FactSummaryComponent } from './fact-summary/fact-summary.component';
import { PowerbiComponent } from './powerbi/powerbi.component';
import { FactCheckingPanelComponent } from './fact-checking-panel/fact-checking-panel.component';
import { FactPaneComponent } from './fact-pane/fact-pane.component';

import { VgCoreModule } from 'videogular2/core';
import { VgControlsModule } from 'videogular2/controls';
import { VgOverlayPlayModule } from 'videogular2/overlay-play';
import { VgBufferingModule } from 'videogular2/buffering';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { NgZorroAntdModule, NZ_I18N, en_US } from 'ng-zorro-antd';
import { registerLocaleData } from '@angular/common';
import en from '@angular/common/locales/en';

registerLocaleData(en);

@NgModule({
  declarations: [
    AppComponent,
    TimestampComponent,
    VideoViewerComponent,
    SpeechViewerComponent,
    FactSummaryComponent,
    PowerbiComponent,
    FactCheckingPanelComponent,
    FactPaneComponent,
  ],
  imports: [BrowserModule, RoutingModule, VgCoreModule, VgControlsModule, VgOverlayPlayModule, VgBufferingModule, BrowserAnimationsModule, FormsModule, HttpClientModule, NgZorroAntdModule],
  providers: [{ provide: NZ_I18N, useValue: en_US }],
  bootstrap: [AppComponent],
})
export class AppModule {}
