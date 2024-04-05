def reward_function(params):
    # lendo os parâmetros de entrada
    all_wheels_on_track = params['all_wheels_on_track']  # parâmetro que verifica se todas as rodas estão na pista
    speed = params['speed']                              # parâmetro que representa a velocidade do carro
    track_width = params['track_width']                  # parâmetro da largura da pista
    distance_from_center = params['distance_from_center']  # parâmetro da distância do centro da pista
    steering = abs(params['steering_angle'])  # parâmetro contendo o ângulo de direção
    # inicializando a recompensa
    reward = 1.0
    # recompensa por permanecer na pista
    if all_wheels_on_track:
        reward += 10.0
    else:
        reward = 1e-3  # recompensa baixa se o carro estiver fora da pista
    # penalizando se o carro estiver muito longe do centro
    distance_penalty = distance_from_center / (track_width / 2)
    reward *= (1 - distance_penalty)
    # recompensando velocidades mais altas
    reward += speed ** 2
    # penalizando ângulos de direção grande
    steering_penalty = steering / 45  # normalizando com base no ângulo máximo de direção
    reward *= (1 - steering_penalty)
    # retornando recompensa
    return reward