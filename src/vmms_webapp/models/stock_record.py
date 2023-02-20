"""Stock Record."""

from datetime import datetime

from sqlalchemy import INTEGER, Column, DateTime, ForeignKey

from vmms_webapp.models.base import Base


class StockRecord(Base):
    """
    A class used to represent a stock record.

    Attributes:
        time_stamp (DateTime): A time stamp in which the stock is recorded
        vm_id (int): A vending machine identification
        prod_id (int): A product identification
        stock (int): A product stock inside the vending machine
    """

    __tablename__ = "stock_records"

    time_stamp = Column(DateTime, default=datetime.utcnow(), primary_key=True)
    vm_id = Column(INTEGER, ForeignKey("vending_machines.id"), primary_key=True)
    prod_id = Column(INTEGER, ForeignKey("products.id"), primary_key=True)
    stock = Column(INTEGER)

    def __init__(
        self,
        vm_id: int,
        prod_id: int,
        stock: int,
        time_stamp: DateTime = datetime.utcnow(),
    ) -> None:
        """Initialize StockRecord.

        Args:
            vm_id (int): A vending machine identification
            prod_id (str): A product identification
            stock (float): A product stock inside the vending machine
            time_stamp (DateTime): A time stamp in which the stock is recorded
        """
        self.time_stamp = time_stamp
        self.vm_id = vm_id
        self.prod_id = prod_id
        self.stock = stock

    def __repr__(self) -> str:
        """Return a string as a representation of the object.

        Returns:
            str: A string representation of the object
        """
        return (
            f"<StockRecord {(self.time_stamp, self.vm_id, self.prod_id)}: {self.stock}>"
        )

    def __eq__(self, other: object) -> bool:
        """Check equality of both instances.

        Returns:
            bool: True if the both instances are equal else False
        """
        if isinstance(other, StockRecord):
            return (
                self.time_stamp == other.time_stamp
                and self.vm_id == other.vm_id
                and self.prod_id == other.prod_id
            )
        return False

    def to_dict(self) -> dict:
        """Convert the object to dictionary.

        Returns:
            dict: A dictionary representing the object
        """
        return {
            "time_stamp": self.time_stamp,
            "vm_id": self.vm_id,
            "prod_id": self.prod_id,
            "stock": self.stock,
        }
