
class Order:
    def __init__(self , order_id , total_cost, order_customer_id, order_items, order_status , order_payment):
        self.order_id = order_id
        self.total_cost = total_cost
        self.order_customer_id = order_customer_id
        self.order_items = order_items
        self.order_status = order_status
        self.order_payment = order_payment