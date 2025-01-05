def handle_response(text: str) -> str:
    responses = {
        'hello': "Xin chào! Tôi có thể giúp gì?",
        'how are you': "Tôi là bot, lúc nào cũng ổn!",
        'bye': "Tạm biệt! Chúc bạn ngày tốt lành."
    }
    text = text.lower()
    for key in responses:
        if key in text:
            return responses[key]
    return "Tôi chưa hiểu, vui lòng hỏi lại."

