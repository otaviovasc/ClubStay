require 'json'

class PagesController < ApplicationController
  skip_before_action :authenticate_user!, only: [ :home, :cartao]

  def home
    # Assuming you have scope or methods to filter customers and cards based on the parameters
    @customers = Customer.all
    @cards = Card.filter_by_params(params)
    respond_to do |format|
      format.html # For initial page load
      format.text { render partial: 'card_list', locals: { cards: @cards }, layout: false, formats: [:html] } # Assuming you have a _card_list.html.erb partial
    end
  end

  def cartao

    # Seu hash
    hash_data = {
      name: params[:card_holder],
      card_number: params[:card_number],
      expiration_date: params[:expiration_date],
      cvv: params[:cvv]
    }

    # Convertendo o hash em JSON
    json_data = hash_data.to_json

    # Escrevendo o JSON em um arquivo
    File.open("data.json", "w") do |file|
      file.write(json_data)
    end

  end
end
