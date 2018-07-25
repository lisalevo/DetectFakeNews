import { Injectable } from '@angular/core';
import { Observable, Subject } from '../../../node_modules/rxjs';

const jsonResponse = require('./response.json');

export interface TimeToClaimMap {
  [time: number]: Claim;
}

@Injectable({
  providedIn: 'root',
})
export class FactCheckService {
  claims: Claim[] = [];
  claims$: Subject<Claim[]> = new Subject();
  parsedClaims: Claim[] = [];
  map: TimeToClaimMap = {};

  constructor() {
    this.parsedClaims = jsonResponse as Claim[];
    this.parsedClaims.forEach(claim => {
      this.map[claim.timeStamp] = claim;
    });
  }

  getClaims(): Observable<Claim[]> {
    return this.claims$.asObservable();
  }

  getClaimAtTime(time: number) {
    if (time in this.map) {
      // console.log('found claim', this.map[time]);
      this.claims.push(this.map[time]);
      this.claims$.next(this.claims);
    }
  }
}
