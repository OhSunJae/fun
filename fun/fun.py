import random

def get_robot_mood(battery, motor_temp, workload):
    print(f"--- 🤖 로봇 상태 점검: 배터리 {battery}% | 온도 {motor_temp}도 | 작업량 {workload}% ---")
    
    if battery < 10:
        return "🪫 배터리 없어요... 배고파서 현기증 난단 말이에요. (기절 직전)"
    elif motor_temp > 80:
        return "🔥 아뜨거! 모터 터지겠어요! 파업하겠습니다. (분노)"
    elif workload > 90:
        return "😫 일이 너무 많아요! 저도 워라밸이 필요합니다. (번아웃)"
    elif battery > 90 and motor_temp < 40:
        return "✨ 컨디션 최고! 지금이라면 화성도 갈 수 있어요! (행복)"
    else:
        greetings = ["👍 적당히 할만하네요.", "🥱 조금 졸린데 한 판 더 하죠.", "🤖 삐리비립. 정상 작동 중."]
        return random.choice(greetings)

if __name__ == "__main__":
    # 랜덤한 상황들 테스트
    print(get_robot_mood(5, 40, 20))    # 배터리 부족
    print(get_robot_mood(95, 30, 10))   # 컨디션 최고
    print(get_robot_mood(50, 85, 50))   # 과열
    print(get_robot_mood(50, 45, 50))   # 평범