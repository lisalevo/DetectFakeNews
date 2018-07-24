import { TestBed, inject } from '@angular/core/testing';

import { FactCheckService } from './fact-check.service';

describe('FactCheckService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [FactCheckService]
    });
  });

  it('should be created', inject([FactCheckService], (service: FactCheckService) => {
    expect(service).toBeTruthy();
  }));
});
