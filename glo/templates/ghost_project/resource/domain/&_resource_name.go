package &_{resource_name}

import (
	"context"
	"github.com/limoxi/ghost"
	db_&_{resource_name} "&_{service_name}/db/&_{resource_name}"
	"time"
)

type &_{resource_title} struct {
	ghost.DomainModel
	Id int
	CreatedAt time.Time
}

func New&_{resource_title}FromDbModel(ctx context.Context, dbModel *db_&_{resource_name}.&_{resource_title}) *&_{resource_title}{
	inst := new(&_{resource_title})
	inst.SetCtx(ctx)
	inst.NewFromDbModel(inst, dbModel)
	return inst
}

func New&_{resource_title}(ctx context.Context) *&_{resource_title}{
	dbModel := &db_&_{resource_name}.&_{resource_title}{}
	db := ghost.GetDBFromCtx(ctx)
	result := db.Create(dbModel)
	if err := result.Error; err != nil{
		panic(ghost.NewSystemError(err.Error(), "创建失败"))
	}
	return &&_{resource_title}{
		Id: dbModel.Id,
	}
}
