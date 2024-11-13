package common

import (
	"context"
	"sync"
)

func MergeContexts(ctxs ...context.Context) (context.Context, context.CancelFunc) {
	ctx, cancel := context.WithCancel(context.Background())
	var wg sync.WaitGroup

	for _, c := range ctxs {
		wg.Add(1)
		go func(c context.Context) {
			defer wg.Done()
			select {
			case <-c.Done():
				cancel() // Cancel the derived context if any parent context is done
			case <-ctx.Done():
			}
		}(c)
	}

	go func() {
		wg.Wait()
		cancel() // Ensure derived context is canceled when all goroutines complete
	}()

	return ctx, cancel
}