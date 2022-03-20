package main

import (
	"testing"
)

func TestAdder(t *testing.T) {
	res := adder(1, 1)
	if res != 2 {
		t.Errorf("expected 2, got: %d", res)
	}
	
}

func TestAdderB(t *testing.T) {
	res := adder(2, 1)
	if res != 3 {
		t.Errorf("expected 3, got: %d", res)
	}
}
