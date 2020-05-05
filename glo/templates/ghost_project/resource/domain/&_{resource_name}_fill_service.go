package &_{resource_name}

import (
	"context"
	"github.com/limoxi/ghost"
)

type &_{resource_title}FillService struct {
	ghost.DomainObject
}

func (this *&_{resource_title}FillService) Fill(&_{resource_plural} []*&_{resource_title}, fillOptions ghost.FillOptions){

}

func New&_{resource_title}FillService(ctx context.Context) *&_{resource_title}FillService{
	inst := new(&_{resource_title}FillService)
	inst.SetCtx(ctx)
	return inst
}