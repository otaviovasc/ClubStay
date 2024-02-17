class Card < ApplicationRecord
  belongs_to :customer

  def self.filter_by_params(params)
    cards = self.all

    # Add your filtering logic based on the provided params
    cards = cards.where(card_status: params[:card_status] == "invalid" ? false : true) if params[:card_status].present?

    if params[:risco_de_churn] == "desc" && params[:risco_de_churn].present?
      cards = cards.sort_by { |card| card.customer.risco_de_churn }.reverse
    else
      cards = cards.sort_by { |card| card.customer.risco_de_churn }
    end

    cards
  end
end
