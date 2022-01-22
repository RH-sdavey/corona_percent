from flask import Flask, render_template
import covid_daily

corona = Flask(__name__)


def world_data():
    """return dataset dict for Total world data (Population, Cases, Deaths, Recovered, Infected_Pct)

    :return: dataset for passing to frontend of application
    :rtype: dict
    """
    world = covid_daily.overview(as_json=False)
    world_pop = world.Population.sum()
    total_cases = world.TotalCases.sum()
    total_deaths = world.TotalDeaths.sum()
    total_recovered = world.TotalRecovered.sum()
    total_active = world.ActiveCases.sum()
    return {
        'world_pop': world_pop,
        'total_cases': total_cases,
        'total_deaths': total_deaths,
        'total_recovered': total_recovered,
        'total_active': total_active,
        'cases_pct': round(((total_cases / world_pop) * 100), 8),
        'pct_deaths_cases': round(((total_deaths / total_cases) * 100), 2),
        'pct_recovered_cases': round(((total_recovered / total_cases) * 100), 2),
        'pct_active_cases': round(((total_active / total_cases) * 100), 2),
        'pct_deaths_population': round((total_deaths / (world_pop + total_deaths) * 100), 2),
        'pct_recovered_population': round(((total_recovered / world_pop) * 100), 2),
        'pct_active_population': round(((total_active / world_pop) * 100), 2),
    }


@corona.route('/')
@corona.route('/index.html')
def index():
    return render_template('index.html', data_set=world_data())

if __name__ == '__main__':
    corona.run(debug=False)
