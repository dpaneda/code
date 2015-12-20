#lang racket
(require 2htdp/batch-io)
(require srfi/1)

(fold + 0 (filter odd? (map string->number (read-lines 'stdin))))
