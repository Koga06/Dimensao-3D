// Esse código ta com a luz na posição do vertice inferior esquerdo

attribute vec3 aPos;
attribute vec4 aCor;

const float kAmb = 0.3; // Coeficiente da luz ambiente

const vec3 luzPos = vec3(-0.5, -0.5, -1.0); // Posição da luz
// nesse vec3 luz Pos (x, y, z)
// quando z = -1, a luz ta mais distante
// quando z = -0.33 a luz ta mais perto

varying vec4 vCor;
varying vec3 vPos;
varying vec3 luz;

void main(){
    // Coordenadas do vertice
    gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);

    // RGB * 0.3
    luz = vec3(1.0, 1.0, 1.0) * kAmb;

    // vetor normal saindo do centro
    vec3 normal = vec3(0.0, 0.0, -1.0);

    // vetor direção da luz: posição da luz mais a posição invertida (-apos)
    vec3 luzDir = normalize(luzPos - aPos);

    // o angulo vai ser entre a direção da luz e normal
    float cosA = max(dot(luzDir, normal), 0.0);
    
    // Luz ambiente * intensidade * coseno
    vec3 luzDiff = luz * 0.7 * cosA;

    // Cor (amarelada) vezes a densidade de luz
    vCor = vec4(1.0, 1.0, 0.2, 1.0) * vec4(luzDiff, 1.0);
    vPos = aPos;

}