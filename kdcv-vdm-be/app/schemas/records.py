from pydantic import BaseModel, Field

class RecordBase(BaseModel):
    record_id: str = Field (
        description="Mã số định danh duy nhất của bảng ghi"
    )
    unix_millis_created_time: int = Field (
        description="Thời gian tạo bảng ghi"
    )
    shift: str = Field (
        description="Ca làm việc"
    )
    job_id: str = Field (
        description="Mã số khởi đầu công việc"
    )
    machine_serial: str = Field (
        description="Mã số serial của máy"
    )
    checker: str = Field (
        description="Người kiểm tra"
    )
    confirmer: str = Field (
        description="Người xác nhận"
    )

    class Config:
        from_attributes = True

class SubdivisionABase(BaseModel):
    record_id: str = Field (
        description="Mã số bản ghi"
    )
    mpa: float = Field (
        description="Đơn vị đo áp suất MPa"
    )
    kgf_per_cm2: float = Field (
        description="Đơn vị đo áp suất kgf/cm2"
    )
    result: str = Field (
        description="Phán định"
    )

    class Config:
        from_attributes = True

class SubdivisionBBase(BaseModel):
    record_id: str = Field (
        description="Mã số bản ghi"
    )
    mpa: float = Field (
        description="Đơn vị đo áp suất MPa"
    )
    kgf_per_cm2: float = Field (
        description="Đơn vị đo áp suất kgf/cm2"
    )
    result: str = Field (
        description="Phán định"
    )

    class Config:
        from_attributes = True

class SubdivisionCBase(BaseModel):
    record_id: str = Field (
        description="Mã số bản ghi"
    )
    mpa: float = Field (
        description="Đơn vị đo áp suất MPa"
    )
    kgf_per_cm2: float = Field (
        description="Đơn vị đo áp suất kgf/cm2"
    )
    result: str = Field (
        description="Phán định"
    )

    class Config:
        from_attributes = True

class SubdivisionSpecialBase(BaseModel):
    record_id: str = Field (
        description="Mã số bản ghi"
    )
    time: int = Field (
        description="Số lần ghi chép"
    )
    reason: str = Field (
        description="Nguyên nhân ghi chép"
    )
    result_bf: str = Field (
        description="Phán định trước thiết định"
    )
    result_af: str = Field (
        description="Phán định sau thiết định"
    )
    result: str = Field (
        description="Phán định"
    )

    class Config:
        from_attributes = True

class Record(RecordBase):
    subdivision_A: list[SubdivisionABase]
    subdivision_B: list[SubdivisionBBase]
    subdivision_C: list[SubdivisionCBase]
    subdivision_special: list[SubdivisionSpecialBase]

class SubdivisionA(SubdivisionABase):
    record: Record

class SubdivisionB(SubdivisionBBase):
    record: Record

class SubdivisionC(SubdivisionCBase):
    record: Record

class SubdivisionSpecial(SubdivisionSpecialBase):
    record: Record

class SubdivisionAId(SubdivisionABase):
    id: int | None = Field(
        default = None
    )

class SubdivisionBId(SubdivisionBBase):
    id: int | None = Field(
        default = None
    )

class SubdivisionCId(SubdivisionCBase):
    id: int | None = Field(
        default = None
    )

class SubdivisionSpecialId(SubdivisionSpecialBase):
    id: int | None = Field(
        default = None
    )
