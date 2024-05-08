from datetime import date
from pydantic import BaseModel, Field   

class JobBase(BaseModel):
    job_id: str = Field (
        description="Mã số khởi đầu công việc"
    )
    job_name: str = Field (
        description="Tên thao tác"
    )
    drafted_place: str = Field (
        description="Nơi soạn thảo"
    )
    drafter: str = Field (
        description="Người soạn thảo"
    )

    class Config:
        from_attributes = True

class JobCategoryBase(BaseModel):
    job_id: str = Field (
        description="Mã số khởi đầu công việc"
    )
    step: int = Field (
        description="Số thứ tự của bước điểm kiểm"
    )
    checkpoint_category: str = Field (
        description="Hạng mục điểm kiểm"
    )
    checkpoint_method: str = Field (
        description="Phương pháp điểm kiểm"
    ) 
    checkpoint_position: str = Field (
        description="Vị trí điểm kiểm"
    )
    confirmation_explanation: str = Field (
        description="Phương pháp xác nhận & bản Thuyết minh kỹ thuật"
    )
    device_change: bool = Field (
        description="Thay đổi thiết bị"
    )
    part_code_change: bool = Field (
        description="Thay đổi mã hàng"
    )
    power_outage: bool = Field (
        description="Cúp điện/điện chập chờn"
    )
    is_measure: bool = Field (
        description="Hạng mục có sử dụng đo hay không"
    )
    is_auto: bool = Field (
        description="Hạng mục lấy dữ liệu từ máy để đánh giá hay không"
    )
    A_sub: bool = Field (
        description="Phân khu A"
    )
    B_sub: bool = Field (
        description="Phân khu B"
    )
    C_sub: bool = Field (
        description="Phân khu C"
    )

    class Config:
        from_attributes = True

# class CheckpointMethodBase(BaseModel):
#     desc: str = Field(
#         description="Mô tả phương pháp điểm kiểm"
#     )
#     position: str = Field(
#         description="Vị trí điểm kiểm"
#     )
#     confirmation_explanation: str = Field(
#         description="Phương pháp xác nhận & bản Thuyết minh kỹ thuật"
#     )
#     is_measure: bool = Field(
#         description="Phương pháp này có đo hay không"
#     )
#     is_auto: bool = Field(
#         description="Phương pháp này có lấy dữ liệu từ máy hay không"
#     )
#     job_category_id: int = Field(
#         description="Mã ID của hạng mục điểm kiểm"
#     )

#     class Config:
#         from_attributes = True

class MachineBase(BaseModel):
    serial_no: str = Field (
        description="Số serial của máy"
    )
    species: str = Field (
        description="Chủng loại máy"
    )
    name: str = Field (
        description="Tên máy"
    )
    job_id: str = Field (
        description="Mã số khởi đầu công việc"
    )
    
    class Config:
        from_attributes = True

class Job(JobBase):
    drafted_date: int = Field (
        description="Ngày soạn thảo"
    )
    updated_date: int = Field (
        description="Ngày cải chính"
    )
    machines: list[MachineBase]
    jobCategories: list[JobCategoryBase]

class JobCategory(JobCategoryBase):
    job: Job
    # checkpoint_method: list[CheckpointMethodBase]

class JobCategoryId(JobCategoryBase):
    id: int | None = Field(
        default = None
    )

# class CheckpointMethod(CheckpointMethodBase):
#     job_category: JobCategory

# class CheckpointMethodId(CheckpointMethodBase):
#     id: int | None = Field(
#         default = None
#     )

class Machine(MachineBase):
    job: Job