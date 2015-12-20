#lang racket                                                                      
(require 2htdp/batch-io)                                                          
                                                                                  
(define (solve l)                                                                 
        (if (or (null? l) (null? (cdr l))) (void)
                          (and (displayln (cadr l)) (solve (cddr l)))))
                                                                                  
(solve (read-lines 'stdin))
