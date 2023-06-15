from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models import WorkerIn, WorkerOut
from database import get_session, Worker
from models.worker import WorkersOut

router = APIRouter(prefix="/worker", tags=["worker"])


@router.get("/get", response_model=WorkerOut)
async def get_one(worker_id: int,
                  session: Session = Depends(get_session)):
    worker: Worker = session.query(Worker).get(worker_id)
    if worker:
        worker_dto = WorkerOut(**worker.__dict__)
        return worker_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"Worker with id {worker_id} not found!")


@router.get("/get_all", response_model=WorkersOut)
async def get_all():
    session = get_session()
    workers = session.query(Worker).all()
    workers_dto = list(map(lambda worker: WorkerOut(**worker.__dict__), workers))
    return WorkersOut(workers=workers_dto)


@router.post("/create_worker", response_model=WorkerOut)
async def create_worker(worker: WorkerIn):
    session = get_session()
    orm_worker = Worker(**worker.dict())
    session.add(orm_worker)
    print(orm_worker.__dict__)
    session.commit()
    print(orm_worker.__dict__)
    worker_dto = WorkerOut(**orm_worker.__dict__)
    return worker_dto


@router.delete("/delete_worker/{worker_id}", response_model=WorkerOut)
async def delete_worker(worker_id: int, session: Session = Depends(get_session)):
    worker: Worker = session.query(Worker).get(worker_id)
    if worker:
        worker_dto = WorkerOut(**worker.__dict__)
        session.delete(worker)
        session.commit()
        return worker_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"Worker with id {worker_id} not found!")


@router.post("/update_workert", response_model=WorkerOut)
async def update_worker(worker: WorkerIn):
    session = get_session()

    orm_worker = session.query(Worker).get(worker.worker_id)
    #session.add(orm_worker)
    orm_worker.fullname = worker.fullname
    orm_worker.jobrank = worker.jobrank
    orm_worker.salary = worker.salary

    print(orm_worker.__dict__)
    session.commit()
    worker_dto = WorkerOut.from_orm(orm_worker)
    return worker_dto