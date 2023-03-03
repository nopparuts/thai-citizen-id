from .validate import validate as _validate
from .address_code import AddressCode as _AddressCode


def extract(citizen_id: str) -> dict[str, str]:
    if (_validate(citizen_id) == False):
        raise ValueError("Citizen ID is not valid")

    person_type = __person_type(citizen_id)
    born_address = __born_address(citizen_id)
    first_order = __first_order(citizen_id)
    second_order = __second_order(citizen_id)
    return {
        'person_type': person_type,
        'born_address': born_address,
        'first_order': first_order,
        'second_order': second_order
    }


def __person_type(citizen_id: str) -> str:
    # Extract person type from first digit in citizen id
    data_dict = {
        '1': 'คนที่เกิดและมีสัญชาติไทยและได้แจ้งเกิดภายในกำหนดเวลา',
        '2': 'คนที่เกิดและมีสัญชาติไทยได้แจ้งเกิดเกินกำหนดเวลา',
        '3': 'คนไทยและคนต่างด้าวที่มีใบสำคัญประจำตัวคนต่างด้าวและมีชื่ออยู่ในทะเบียนบ้านในสมัยเริ่มแรก',
        '4': 'คนไทยและคนต่างด้าวที่มีใบสำคัญคนต่างด้าว แต่แจ้งย้ายเข้าโดยยังไม่มีเลขประจำตัวประชาชนในสมัยเริ่มแรก',
        '5': 'คนไทยที่ได้รับอนุมัติให้เพิ่มชื่อเข้าไปในทะเบียนบ้านในกรณีตกสำรวจหรือกรณีอื่น ๆ',
        '6': 'ผู้ที่เข้าเมืองโดยไม่ชอบด้วยกฎหมาย และผู้ที่เข้าเมืองโดยชอบด้วยกฎหมายแต่อยู่ในลักษณะชั่วคราว',
        '7': 'บุตรของบุคคลประเภทที่ 6 ซึ่งเกิดในประเทศไทย',
        '8': 'คนต่างด้าวที่เข้าเมืองโดยถูกต้องตามกฎหมาย',
        '9': 'บุคคลที่ไม่มีสถานะทางทะเบียนราษฎร ไม่มีสัญชาติและยังไม่ได้รับการให้สัญชาติไทย ได้รับการผ่อนผันให้อาศัยอยู่ในประเทศไทยได้ชั่วคราว'
    }
    return data_dict[citizen_id[0]]


def __born_address(citizen_id: str) -> str:
    # Extract born address from citizen id

    address_code = _AddressCode()
    try:
        return address_code.address_code[citizen_id[1:5]]
    except KeyError:
        return 'Not found'


def __first_order(citizen_id: str) -> int:
    # Extract first order from citizen id
    return int(citizen_id[5:10])


def __second_order(citizen_id: str) -> int:
    # Extract second order from citizen id
    return int(citizen_id[10:12])
