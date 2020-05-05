package &_{resource_name}

import (
	"context"
	"github.com/limoxi/ghost"
	db_&_{resource_name} "&_{service_name}/db/&_{resource_name}"
)

type &_{resource_title}Repository struct {
	ghost.BasDomainRepository
}

func (this *&_{resource_title}Repository) GetByFilters(filters ghost.Map) []*&_{resource_title}{
	ctx := this.GetCtx()
	db := ghost.GetDBFromCtx(ctx).Model(&db_&_{resource_name}.&_{resource_title}{}).Where(filters)
	var dbModels []*db_&_{resource_name}.&_{resource_title}
	if this.Paginator != nil{
		this.Paginator.Paginate(db)
	}
	result := db.Order("-id").Find(&dbModels)
	if err := result.Error; err != nil{
		panic(err)
	}

	&_{resource_plural} := make([]*&_{resource_title}, 0)
	for _, dbModel := range dbModels{
		&_{resource_plural} = append(&_{resource_plural}, New&_{resource_title}FromDbModel(ctx, dbModel))
	}
	return &_{resource_plural}
}

func (this *&_{resource_title}Repository) GetById(&_{resource_name}Id int) *&_{resource_title}{
	&_{resource_plural} := this.GetByFilters(ghost.Map{
		"id": &_{resource_name}Id,
	})
	if len(&_{resource_plural}) > 0{
		return &_{resource_plural}[0]
	}
	return nil
}

func New&_{resource_title}Repository(ctx context.Context) *&_{resource_title}Repository{
	inst := new(&_{resource_title}Repository)
	inst.SetCtx(ctx)
	return inst
}
