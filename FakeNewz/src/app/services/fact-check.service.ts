import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class FactCheckService {
  claims: Claim[] = [];

  claim1: Claim = {
    timeStamp: 132,
    claim: 'What was said that can be proven',
    supportingDocURL: 'http:/politico.com',
    supportingDocSummary: 'Summary of the supporting documentation.',
    supportingImg: 'https://picsum.photos/200/random',
  };
  claim2: Claim = {
    timeStamp: 132,
    claim: 'What was said that can be proven',
    supportingDocURL: 'http:/politico.com',
    supportingDocSummary: 'Summary of the supporting documentation.',
    supportingImg: 'https://picsum.photos/200/random',
  };
  claim3: Claim = {
    timeStamp: 132,
    claim: 'What was said that can be proven',
    supportingDocURL: 'http:/politico.com',
    supportingDocSummary: 'Summary of the supporting documentation.',
    supportingImg: 'https://picsum.photos/200/random',
  };
  claim4: Claim = {
    timeStamp: 132,
    claim: 'What was said that can be proven',
    supportingDocURL: 'http:/politico.com',
    supportingDocSummary: 'Summary of the supporting documentation.',
    supportingImg: 'https://picsum.photos/200/random',
  };

  constructor() {
    this.claims.push(this.claim1);
    this.claims.push(this.claim2);
    this.claims.push(this.claim3);
    this.claims.push(this.claim4);
  }

  getClaims(): Claim[] {
    return this.claims;
  }
}
