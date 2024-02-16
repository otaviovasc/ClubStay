require 'csv'
require 'faker'


csv_file_path = '../data/socio_torcedor.csv'

Card.destroy_all
Customer.destroy_all
puts "Deleting all customers"
puts "Deleting all cards"

CSV.foreach(csv_file_path, headers: true).with_index do |row, index|
  Customer.create(
    name: Faker::Name.name,
    email: Faker::Internet.email,
    team_id: 1,
    tempo_de_assinatura: row['tempo_de_assinatura'],
    historico_de_presenca_nos_jogos: row['historico_de_presenca_nos_jogos'],
    historico_de_socio: row['historico_de_socio'],
    numero_de_desistencias_no_periodo: row['numero_de_desistencias_no_periodo'],
    historico_de_preco_nos_planos: row['historico_de_preco_nos_planos'],
    tipo_de_plano: row['tipo_de_plano'],
    quantos_membros: row['quantos_membros'],
    planos_com_ingresso_incluso: row['planos_com_ingresso_incluso'] == 'sim',
    estado_civil: row['estado_civil'],
    risco_de_churn: row['risco_de_churn'],
    feedback_sobre_servicos: row['feedback_sobre_servicos'],
    frequencia_de_compra_de_produtos: row['frequencia_de_compra_de_produtos']
  )
end

puts "Customers Created"

cardNumber = [4242424242424242, 4000056655699556, 5555555555554444, 2223003122003222, 5200828282828210, 5105105105105100]

Customer.all.each.with_index do |customer, index|
  Card.create!(
    number: cardNumber[index % 6],
    cvc: rand(100...999),
    exp_month: rand(1...12),
    exp_year: rand(2025...2040),
    customer_id: customer.id
  )
end

puts "Cards created"
